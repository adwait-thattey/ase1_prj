import threading
import subprocess
from .docker import Docker
from django.db import connection

from .models import TestCase
import os


class RunAndAssert(threading.Thread):
    def __init__(self, thread_id, result_instance, code_file=None):
        """

        :param thread_id: Give an id to the thread
        :param result_instance: An instance of the result model
        :param code_file: Provide this file if you are doing any pre-processing on user \
        submitted code. For ex. If user is giving code in c++, compile it in pre-processing\
         and pass the a.out file here.

        """
        super().__init__()
        self.result = result_instance
        self.id = thread_id

        if code_file is None:
            self.code = result_instance.submission.code.path
        else:
            self.code = code_file

        # dir = os.path.dirname(self.code)
        # dir = os.path.join(dir, str(self.result.testcase.id))
        #
        # if not os.path.exists(dir):
        #     os.makedirs(dir)

        # self.error = os.path.join(dir, "error.txt")
        # self.output = os.path.join(dir, "output.txt")
        self.result_code = -1

        self.docker_instance = Docker(
            unique_code="cont" + str(self.result.id),
            code_file=self.code,
            input_file=self.result.testcase.input_file.path,
            time_limit=self.result.submission.question.time_limit
        )

    def run_code(self):
        # fi = open(self.result.testcase.input_file.path, mode="r")
        # fo = open(self.output, mode="w")
        # fe = open(self.error, mode="w")

        # try:

            # code_result = subprocess.run(["python3", self.code], stdin=fi, stdout=fo, stderr=fe,
            #                              timeout=self.result.submission.question.time_limit)

        # TODO Add support for more languages

        code_status = self.docker_instance.run_code_and_return_status()
        if code_status == 124:
            self.result_code = -5

        elif code_status == -1:
            self.result_code = -1

        else:
            self.result_code = 0

        #     # fe.close()
        #     if os.stat(self.error).st_size == 0:
        #         self.result_code = 0
        #     else:
        #         self.result_code = -1
        #
        # except subprocess.TimeoutExpired:
        #     self.result_code = -5

        # TODO Set timeout

        # fi.close()
        # fo.close()

    def assert_output(self):
        exp_output = self.result.testcase.output_file.path

        f1 = open(exp_output, mode="r")
        f2 = open(self.docker_instance.output_file, mode="r")

        result = False
        if f1.read() == f2.read():
            result = True

        f1.close()
        f2.close()

        return result

    def run(self):

        self.result.pass_fail = 5
        self.result.save()

        self.run_code()
        if self.result_code == 0:
            result = self.assert_output()
            if result:
                self.result.pass_fail = 1
            else:
                self.result.pass_fail = 4

        elif self.result_code == -1:
            fe = open(self.docker_instance.error_file, mode="r")
            self.result.pass_fail = 3
            self.result.errors = fe.read()
            fe.close()

        elif self.result_code == -5:
            self.result.pass_fail = 2

        else:
            raise ValueError("Unknown value of result_code")

        self.result.save()

        self.teardown()

    def teardown(self):
        self.docker_instance.delete_dir()
        connection.close()


class LimitThreads(threading.Thread):
    def __init__(self, thread_id, thread_list):
        """

        :param thread_id:
        :param thread_list:
        """

        super().__init__()
        self.thread_id = thread_id
        self.thread_list = thread_list

    def run(self):
        # print("chunk start")
        for thr in self.thread_list:
            thr.start()
            thr.join()

        # print("chunk end")

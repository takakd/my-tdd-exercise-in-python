class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def setUp(self):
        self.wasRun = None
        self.log = "setUp "
    def testMethod(self):
        self.wasRun = True
        self.log = self.log + "testMethod "


# Test
class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetup(self):
        self.test.run()
        assert("setUp testMethod " == self.test.log)

TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()

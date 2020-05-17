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
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)
    def setUp(self):
        self.wasSetUp = True
    def testMethod(self):
        self.wasRun = True


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

    def testSetup(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()

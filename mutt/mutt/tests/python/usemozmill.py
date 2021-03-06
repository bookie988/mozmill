import os
import tempfile
import unittest
import mozmill
from mozmill.logger import LoggerListener

class ModuleTest(unittest.TestCase):
    def test_modules(self):
        testpath = os.path.join("..", "js", "test_testmodules.js")
        self.do_test(testpath, passes = 1, fails = 0, skips = 0)
        testpath = os.path.join("..", "js", "test_testmodules2.js")
        # TODO: Uncomment this when the bug is fixed
        #self.do_test("../js/test_testmodules2.js", passes = 0, fails = 0, skips = 1)

    def do_test(self, relative_test_path, passes = 0, fails = 0, skips = 0):
        testpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_test_path)
        print "this is testpath: %s" % testpath
        
        test = [{'path': testpath}]
        log_file = tempfile.mktemp(suffix='.txt')
        print "this is logfile: %s" % log_file
        logger = LoggerListener(log_file=log_file, file_level="DEBUG", debug=True)
        m = mozmill.MozMill.create(handlers=(logger,), runner_args={'cmdargs':['-console']})
        results = m.run(*test)
        results.finish((logger,))
        
        # From the first test, there is one passing test
        self.assertEqual(len(results.passes), passes, "Passes should match")
        self.assertEqual(len(results.fails), fails, "Fails should match")
        self.assertEqual(len(results.skipped), skips, "Skips should match")

if __name__ == '__main__':
    unittest.main()

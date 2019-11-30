from src.Execution import Execution

import unittest

class ExecutionTestCase( unittest.TestCase ):

    def testExecute( self ):
        execution = Execution()

        execution.execute( "add", 1, 2 )

        self.assertEqual( execution.mALUResult, 3 )

if __name__ == '__main__':  
    unittest.main()
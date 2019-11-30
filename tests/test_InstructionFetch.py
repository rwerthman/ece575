from src.InstructionFetch import InstructionFetch

import unittest

class InstructionFetchTestCase( unittest.TestCase ):

    def testExecute( self ):

        instructionMemory = [
            [ "instruction1" ],
            [ "instruction2" ]
        ]

        IF = InstructionFetch( instructionMemory )

        IF.execute()

        self.assertEqual( IF.mInstruction, [ "instruction1" ] )
        self.assertEqual( IF.mPC, 1 )

if __name__ == '__main__':  
    unittest.main()
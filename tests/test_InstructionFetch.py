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

        self.assertEqual( IF.instruction, [ "instruction1" ] )
        self.assertEqual( IF.PC, 1 )

if __name__ == '__main__':  
    unittest.main()
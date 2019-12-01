from src.CPU import CPU

import unittest

class CPUTestCase( unittest.TestCase ):

    def testCycle( self ):
        instructionMemory = [
            [ "add", "r1", "r2", "r3" ],
        ]

        cpu = CPU( instructionMemory )
        cpu.cycle()
        
        self.assertEqual( cpu.ID.readFromRegister( "r3" ), 3 )

if __name__ == '__main__':  
    unittest.main()
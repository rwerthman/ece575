from src.CPU import CPU

import unittest

class CPUTestCase( unittest.TestCase ):

    def testCycleAdd( self ):

        # $r3 = $r1 + $r2
        instructionMemory = [
            [
                "add", # op
                "r1",  # rs
                "r2",  # rt
                "r3"   # rd
            ]
        ]

        cpu = CPU( instructionMemory )
        cpu.cycle()
        
        self.assertEqual( cpu.ID.readFromRegister( "r3" ), 3 )
    
    def testCycleLoadWord( self ):

        # $r1 = Memory[$r3 + 0]
        instructionMemory = [
            [
                "lw", # op
                "r3", # rs
                "r1", # rt
                0 # address
            ]
        ]

        cpu = CPU( instructionMemory )
        cpu.cycle()
        
        self.assertEqual( cpu.ID.readFromRegister( "r1" ), 1 )

    def testCycleStoreWord( self ):

        # $r1 = Memory[$r3 + 0]
        instructionMemory = [
            [
                "sw", # op
                "r3", # rs
                "r1", # rt
                2 # address
            ]
        ]

        cpu = CPU( instructionMemory )
        cpu.cycle()
        
        self.assertEqual( cpu.MEM.dataMemory[2], 2 )

if __name__ == '__main__':  
    unittest.main()
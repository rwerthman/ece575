from src.InstructionDecode import InstructionDecode

import unittest

class InstructionDecodeTestCase( unittest.TestCase ):
    
    def testRegisterReadWrite( self ):

        ID = InstructionDecode()

        ID.mRegWrite = True
        ID.writeRegister( 'r1', 2 )

        ID.mRegWrite = False

        self.assertEqual( ID.readRegister( 'r1' ), 2 )
    
    def testExecuteRTypeInstruction( self ):
        ID = InstructionDecode()

        instruction = [ "add", "r1", "r2", "r3" ]

        ID.execute( instruction )

        self.assertEqual( ID.mReadRegister1, "r1" )
        self.assertEqual( ID.mReadRegister2, "r2" )
        self.assertTrue( ID.mRegWrite )
        self.assertEqual( ID.mWriteRegister, "r3" )
        self.assertEqual( ID.currentOpCode, "add" )

if __name__ == '__main__':  
    unittest.main()

from src.InstructionDecode import InstructionDecode
from src.ControlUnit import ControlUnit
from src.InstructionFetch import InstructionFetch

import unittest

class InstructionDecodeTestCase( unittest.TestCase ):
    
    def testRegisterReadWrite( self ):

        controlUnit = ControlUnit()
        IF = InstructionFetch( [] )
        ID = InstructionDecode( controlUnit, IF)
        ID.writeRegister = "r1"

        ID.writeToRegister( 2 )

        self.assertEqual( ID.readFromRegister( "r1" ), 2 )
    
    def testExecuteRTypeInstruction( self ):
        controlUnit = ControlUnit()
        IF = InstructionFetch( [[ "add", "r1", "r2", "r3" ]] )
        ID = InstructionDecode( controlUnit, IF)

        IF.execute()

        ID.execute()

        self.assertEqual( ID.readRegister1, "r1" )
        self.assertEqual( ID.readRegister2, "r2" )
        self.assertEqual( ID.writeRegister, "r3" )

if __name__ == '__main__':  
    unittest.main()

from src.Execution import Execution
from src.ControlUnit import ControlUnit
from src.InstructionDecode import InstructionDecode
from src.InstructionFetch import InstructionFetch

import unittest

class ExecutionTestCase( unittest.TestCase ):

    def testExecute( self ):

        controlUnit = ControlUnit()
        IF = InstructionFetch( [] )
        ID = InstructionDecode( controlUnit, IF)

        execution = Execution( controlUnit, ID )

        controlUnit.ALUOp = 0 # add
        ID.writeRegister = "r1"
        ID.writeToRegister( 3 )
        ID.readRegister1 = "r1"
        ID.readRegister2 = "r2"

        execution.execute()

        self.assertEqual( execution.ALUResult, 4 )

if __name__ == '__main__':  
    unittest.main()
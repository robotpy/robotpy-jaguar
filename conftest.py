@pytest.fixture(scope="function")
def frccan(request):
    
    # Not sure how to deal with this yet
    assert False
    
    """Mock for frccan module."""
    frccan = MagicMock(name='mock_frccan')

    class CANError(RuntimeError):
        pass
    class CANMessageNotFound(CANError):
        pass

    frccan.CANError = CANError
    frccan.CANMessageNotFound = CANMessageNotFound

    # Flags in the upper bits of the messageID
    frccan.CAN_IS_FRAME_REMOTE = 0x80000000
    frccan.CAN_IS_FRAME_11BIT = 0x40000000

    return frccan
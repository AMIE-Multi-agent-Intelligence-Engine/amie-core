from app.platform.kernel import CognitiveKernel, KernelState


def test_kernel_lifecycle():
    kernel = CognitiveKernel()
    assert kernel.state is KernelState.CREATED
    assert not kernel.running

    kernel.start()
    assert kernel.running

    kernel.stop()
    assert kernel.state is KernelState.STOPPED

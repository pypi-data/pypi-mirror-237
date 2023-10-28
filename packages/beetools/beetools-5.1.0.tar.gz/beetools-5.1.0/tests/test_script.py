from beetools import script
from beetools import utils


class TestScript:
    def test__do_example(self):
        """Testing script_do_example()"""
        assert script.do_examples()
        pass

    def test__exec_batch(self, self_destruct_work_dir):
        """Testing script_exec_batch()"""

        tmp_test = self_destruct_work_dir.dir / 'test'
        tmp_t1 = tmp_test / 'T1'
        cmds = []
        if utils.get_os() in [utils.LINUX, utils.MACOS]:
            cmds = [
                ['mkdir', '-p', f'{tmp_t1}'],
                ['ls', '-l', f'{tmp_test}'],
            ]
        elif utils.get_os() == utils.WINDOWS:
            cmds = [
                ['md', f'{tmp_t1}'],
                ['dir', '/B', f'{tmp_test}'],
            ]
        assert script.exec_batch(cmds, p_verbose=False) == [0, 0]
        pass

    def test__exec_batch_in_session(self, self_destruct_work_dir):
        """Testing script_exec_batch_in_session()"""
        tmp_test = self_destruct_work_dir.dir / 'test'
        tmp_t1 = tmp_test / 'T1'
        batch = []
        if utils.get_os() in [utils.LINUX, utils.MACOS]:
            batch = [
                f'mkdir -p {tmp_t1}',
                f'ls -l {tmp_test}',
                f'rm -R {tmp_test}',
            ]
        elif utils.get_os() == utils.WINDOWS:
            batch = [
                f'md {tmp_t1}',
                f'dir /B {tmp_test}',
                f'rd /Q /S {tmp_test}',
            ]
        assert script.exec_batch_in_session(batch, p_verbose=False) == 0
        pass

    def test__exec_cmd(self, self_destruct_work_dir):
        """Testing script_exec_cmd()"""
        tmp_dir = self_destruct_work_dir.dir / 'test' / 'T1'
        if utils.get_os() in [utils.LINUX, utils.MACOS]:
            cmd1 = ['mkdir', '-p', f'{tmp_dir}']
            cmd2 = ['touch', f'{tmp_dir}/t.txt']
            cmd3 = ['rmdir', f'{tmp_dir}']
        else:
            cmd1 = ['md', f'{tmp_dir}']
            cmd2 = ['echo.', '>>', f'{tmp_dir}\\t.txt']
            cmd3 = ['rd', f'{tmp_dir}']
        assert script.exec_cmd(cmd1) == 0
        assert script.exec_cmd(cmd2) == 0
        assert script.exec_cmd(cmd3) != 0  # Attempt to remove non-empty directory to create exception

        pass

    def test__write_script(self, self_destruct_work_dir):
        """Testing script_exec_batch()"""
        script_pth = self_destruct_work_dir.dir / __name__
        cmds = [
            ['echo', 'Hello'],
            ['echo', 'Goodbye'],
        ]
        assert script.write_script(script_pth, cmds) == 'echo Hello\necho Goodbye\n'
        pass

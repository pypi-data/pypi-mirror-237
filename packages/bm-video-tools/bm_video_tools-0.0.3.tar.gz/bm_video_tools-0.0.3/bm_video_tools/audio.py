from __future__ import annotations

from .media import Media
from .operate import Operate
from .utils import backslash2slash, subprocess_exec


class Audio(Media):
    async def run(self, op: Operate, output_path: str) -> Audio:
        """
        执行操作
        :param op: Operation实例对象
        :param output_path: 输出路径
        :return: 媒体对象
        """
        output_path = backslash2slash(output_path)

        cmd = op.exec(o_a=True)
        await subprocess_exec(cmd, self.input_path, output_path)

        return self.__class__(output_path)

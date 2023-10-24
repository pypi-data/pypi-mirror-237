import asyncio

from bm_video_tools import Audio, Operate

audio_path = './asset/audio1.mp3'
output_path = './output'


# 查看音频信息
async def test_info():
    audio = Audio(audio_path)
    info = await audio.get_info()
    print(info)


# 修改音频参数
async def test_params():
    audio = Audio(audio_path)
    op = Operate().params(sample='44100')
    await audio.run(op, output_path=f'{output_path}/audio1_params.mp3')


# 音频拆分
async def test_split():
    audio = Audio(audio_path)
    op = Operate().split('00:00:00', second=5)
    await audio.run(op, output_path=f'{output_path}/audio1_split.mp3')


# 倍速播放
async def test_speed():
    audio = Audio(audio_path)
    op = Operate().speed(0.5)
    await audio.run(op, output_path=f'{output_path}/audio1_speed.mp3')


if __name__ == '__main__':
    async def main():
        await asyncio.gather(
            test_info(),
            test_params(),
            test_split(),
            test_speed()
        )


    asyncio.run(main())

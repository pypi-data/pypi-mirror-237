print("= ${__FILE__} in websim  for  ${PLATFORM} =")

# =====================================================
import sys

sys.path.append("${PLATFORM}")


# cannot fake a cpu __WASM__ will be False

# but fake the platform AND the module
sys.platform = "emscripten"


class __EMSCRIPTEN__(object):
    def __init__(self):
        import platform

        self.platform = platform

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except:
            return object.__getattribute__(self.platform, name)

    @classmethod
    def PyConfig_InitPythonConfig(*argv):
        pass

    @classmethod
    def init_platform(*argv):
        pass

    @classmethod
    def flush(cls):
        sys.stdout.flush()
        sys.stderr.flush()

    @classmethod
    def trap(cls, *argv, **kw):
        pass

    @classmethod
    def system(cls):
        return "Linux"

    def run(*argv, **kw):
        ...

    is_browser = False

    js = pdb
    run_script = pdb


__EMSCRIPTEN__ = __EMSCRIPTEN__()

sys.modules["__EMSCRIPTEN__"] = __EMSCRIPTEN__
sys.modules["embed"] = __EMSCRIPTEN__


import aio
import aio.prepro
import aio.cross

aio.cross.simulator = True

# ===============================================================================


async def custom_site():
    while True:
        await asyncio.sleep(0.016)


import asyncio

asyncio.run(custom_site())

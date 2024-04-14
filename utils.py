import settings
import psutil

def get_memory_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss


def height_prct(percentage):
    return (settings.HEIGHT/100)*percentage

def width_prct(percentage):
    return (settings.WIDTH/100)*percentage


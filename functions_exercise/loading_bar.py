def loading(progress: int):
    loading_bar = "%" * int(progress / 10) + "." * int(10 - progress / 10)

    if progress == 100:
        return f"100% Complete!\n[{loading_bar}]"
    else:
        return f"{progress}% [{loading_bar}]\nStill loading..."


load_progress = int(input())
print(loading(load_progress))

from capture import capture, getHotkeyConfig, getDirectoryConfig, changeDirectoryNormalize


if __name__ == "__main__":
    capture(getHotkeyConfig(), changeDirectoryNormalize(
        getDirectoryConfig()), True)

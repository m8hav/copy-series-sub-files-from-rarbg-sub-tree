import os, shutil

print("\n")

# put r before every string to avoid Unicode Error
folder_paths_list = [
    # r"\\wsl.localhost\Ubuntu\mnt\wsl\PHYSICALDRIVE1p2\home\bart\Downloads\Pending\Lucifer.S02.1080p.BluRay.x265-RARBG",
    # r"\\wsl.localhost\Ubuntu\mnt\wsl\PHYSICALDRIVE1p2\home\bart\Downloads\Pending\Lucifer.S03.1080p.BluRay.x265-RARBG",
    # r"\\wsl.localhost\Ubuntu\mnt\wsl\PHYSICALDRIVE1p2\home\bart\Downloads\Pending\Lucifer.S04.1080p.BluRay.x265-RARBG",
    # r"\\wsl.localhost\Ubuntu\mnt\wsl\PHYSICALDRIVE1p2\home\bart\Downloads\Pending\Lucifer.S05.COMPLETE.1080p.NF.WEBRip.DDP5.1.x264-MRCS[rartv]",
    # r"\\wsl.localhost\Ubuntu\mnt\wsl\PHYSICALDRIVE1p2\home\bart\Downloads\Pending\Lucifer.S06.1080p.NF.WEBRip.DDP5.1.x264-AGLET[rartv]",
    # r"\\wsl.localhost\Ubuntu\mnt\wsl\PHYSICALDRIVE1p2\home\bart\Downloads\UPending\Movies and Series\The.Sex.Lives.Of.College.Girls.S01.PROPER.1080p.WEBRip.x265-RARBG",
    r"C:\Users\BartBruh\Downloads\WPending\The.Sex.Lives.Of.College.Girls.S02.1080p.WEBRip.x265-RARBG",
]


for folder_index, folder_path in enumerate(folder_paths_list, start=1):
    if not folder_path: continue
    video_names_list = sorted(os.listdir(folder_path))
    subs_folder_path = folder_path + "/Subs"
    video_index = 1
    if "Subs" in video_names_list:
        for video_name in video_names_list:
            if video_name == "Subs" or video_name.endswith(".srt") or video_name.startswith("RARBG"): continue
            video_name = video_name.replace(".mp4", "").replace(".mkv", "")
            sub_files_folder_path = f"{subs_folder_path}/{video_name}"
            sub_files_names_list = os.listdir(sub_files_folder_path)
            # getting only english files
            sub_files_names_list = [sub_file_name for sub_file_name in sub_files_names_list if "english" in sub_file_name.lower()]
            # getting subtitle file sizes
            sub_files_sizes_list = [os.path.getsize(f"{sub_files_folder_path}/{sub_file_name}") for sub_file_name in sub_files_names_list]
            index_of_sub_file_with_max_size = sub_files_sizes_list.index(max(sub_files_sizes_list))
            chosen_sub_file_name = sub_files_names_list[index_of_sub_file_with_max_size]
            chosen_sub_file_path = f"{sub_files_folder_path}/{chosen_sub_file_name}"
            chosen_sub_file_extension = chosen_sub_file_name.split(".")[-1]
            sub_file_final_name = f"{video_name}.{chosen_sub_file_extension}"
            sub_file_final_path = f"{folder_path}/{sub_file_final_name}"

            try: shutil.copyfile(chosen_sub_file_path, sub_file_final_path)
            except FileExistsError:
                os.remove(sub_file_final_path)
                shutil.copyfile(chosen_sub_file_path, sub_file_final_path)

            print(f"\nVIDEO {video_index}: {sub_file_final_name} - DONE")
            video_index += 1
    folder_name = folder_path.split('\\')[-1]
    print(f"\n\n\nFOLDER {folder_index}: {folder_name} - DONE\n\n")
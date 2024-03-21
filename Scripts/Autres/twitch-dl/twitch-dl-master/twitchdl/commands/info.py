import m3u8

from twitchdl import utils, twitch
from twitchdl.exceptions import ConsoleError
from twitchdl.output import print_video, print_clip, print_json, print_out, print_log


def info(args):
    video_id = utils.parse_video_identifier(args.video)
    if video_id:
        print_log("Fetching video...")
        video = twitch.get_video(video_id)

        if not video:
            raise ConsoleError("Video {} not found".format(video_id))

        print_log("Fetching access token...")
        access_token = twitch.get_access_token(video_id)

        print_log("Fetching playlists...")
        playlists = twitch.get_playlists(video_id, access_token)

        print_log("Fetching chapters...")
        chapters = twitch.get_video_chapters(video_id)

        if args.json:
            video_json(video, playlists, chapters)
        else:
            video_info(video, playlists, chapters)
        return

    clip_slug = utils.parse_clip_identifier(args.video)
    if clip_slug:
        print_log("Fetching clip...")
        clip = twitch.get_clip(clip_slug)
        if not clip:
            raise ConsoleError("Clip {} not found".format(clip_slug))

        if args.json:
            print_json(clip)
        else:
            clip_info(clip)
        return

    raise ConsoleError("Invalid input: {}".format(args.video))


def video_info(video, playlists, chapters):
    print_out()
    print_video(video)

    print_out()
    print_out("Playlists:")
    for p in m3u8.loads(playlists).playlists:
        print_out("<b>{}</b> {}".format(p.stream_info.video, p.uri))

    if chapters:
        print_out()
        print_out("Chapters:")
        for chapter in chapters:
            start = utils.format_time(chapter["positionMilliseconds"] // 1000, force_hours=True)
            duration = utils.format_time(chapter["durationMilliseconds"] // 1000)
            print_out(f'{start} <b>{chapter["description"]}</b> ({duration})')


def video_json(video, playlists, chapters):
    playlists = m3u8.loads(playlists).playlists

    video["playlists"] = [
        {
            "bandwidth": p.stream_info.bandwidth,
            "resolution": p.stream_info.resolution,
            "codecs": p.stream_info.codecs,
            "video": p.stream_info.video,
            "uri": p.uri
        } for p in playlists
    ]

    video["chapters"] = chapters

    print_json(video)


def clip_info(clip):
    print_out()
    print_clip(clip)
    print_out()
    print_out("Download links:")

    for q in clip["videoQualities"]:
        print_out("<b>{quality}p{frameRate}</b> {sourceURL}".format(**q))

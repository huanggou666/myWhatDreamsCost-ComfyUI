import json


class VideoInfoParser:
    """
    Receives the video_info JSON string produced by LoadVideoUI and
    exposes every field as a typed output pin, matching the layout of
    the VideoHelperSuite 'Video Info' node.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "video_info": ("STRING", {"forceInput": True}),
            }
        }

    # Orange = FLOAT  |  Blue = INT  (mirrors VideoHelperSuite colour convention)
    RETURN_TYPES  = ("FLOAT", "INT",   "FLOAT",           "INT",          "INT",           "FLOAT",      "INT",                "FLOAT",          "INT",          "INT")
    RETURN_NAMES  = ("source_fps", "source_frame_count", "source_duration", "source_width", "source_height", "loaded_fps", "loaded_frame_count", "loaded_duration", "loaded_width", "loaded_height")
    FUNCTION      = "parse"
    CATEGORY      = "Custom/Video"
    OUTPUT_NODE   = False

    def parse(self, video_info: str):
        try:
            info = json.loads(video_info)
        except (json.JSONDecodeError, TypeError):
            info = {}

        source_fps         = float(info.get("source_fps",         0.0))
        source_frame_count = int  (info.get("source_frame_count", 0  ))
        source_duration    = float(info.get("source_duration",    0.0))
        source_width       = int  (info.get("source_width",       0  ))
        source_height      = int  (info.get("source_height",      0  ))

        loaded_fps         = float(info.get("loaded_fps",         0.0))
        loaded_frame_count = int  (info.get("loaded_frame_count", 0  ))
        loaded_duration    = float(info.get("loaded_duration",    0.0))
        loaded_width       = int  (info.get("loaded_width",       0  ))
        loaded_height      = int  (info.get("loaded_height",      0  ))

        return (
            source_fps,
            source_frame_count,
            source_duration,
            source_width,
            source_height,
            loaded_fps,
            loaded_frame_count,
            loaded_duration,
            loaded_width,
            loaded_height,
        )


# ── ComfyUI registration ────────────────────────────────────────────────────
NODE_CLASS_MAPPINGS = {
    "VideoInfoParser": VideoInfoParser,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VideoInfoParser": "Video Info Parser",
}

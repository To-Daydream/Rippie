# 🎵 Rippie

> Drop a stone in water, and it ripples outward in every direction. Rippie does the same for music.

Share a song from any platform: Spotify, Apple Music, YouTube Music, etc. and Rippie catches it, then sends it back out across every platform you care about. All in your Discord server.

No more "I don't have Spotify." No more re-searching the same song. One link becomes many.


## What it does

When a music link is posted in a channel Rippie is watching, it responds with the original link alongside buttons for every equivalent platform. Everyone in the server can open the song in whatever service they actually use.

Platform buttons are configurable per server, so you only see the ones that matter to your community.


## Status

🚧 Early development and testing

Currently researching the mainstream platform APIs and available Python libraries to understand how to fetch and match tracks across services — and implementing samples to validate the approach. This replaces the original plan to use the Odesli API, which is being deprecated.

Libraries and APIs under investigation:
- [spotipy](https://github.com/spotipy-dev/spotipy) — Spotify Web API wrapper
- [ytmusicapi](https://github.com/sigma67/ytmusicapi) — Unofficial YouTube Music API
- [apple-music-python](https://apple-music-python.readthedocs.io/en/latest/) — Apple Music API (old but useful for references)

## Planned features

- Detect music links from major platforms automatically
- Resolve cross-platform equivalents by communicating directly with each platform's API
- Reply with platform buttons (Spotify, YouTube Music, Apple Music, SoundCloud, Tidal, and more)
- Per-server configuration for which platforms to show

## Built with

- [pycord](https://pycord.dev/)
- [uv](https://docs.astral.sh/uv/)
- [ruff](https://docs.astral.sh/ruff/)

## Contributing

Not ready for contributions yet, but feel free to open issues with ideas or feedback.
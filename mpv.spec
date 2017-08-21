Name:       mpv
Version:    0.26.0
Release:    7635%{?dist}
Summary:    Movie player playing most video formats and DVDs

Group:      Unspecified
License:    GPLv2+
URL:        http://mpv.io/
Source0:    https://github.com/mpv-player/mpv/archive/v0.26.0.tar.gz

BuildRequires: autoconf automake libtool freetype-devel fribidi-devel fontconfig-devel yasm-devel mesa-libgbm-devel libass-devel libbluray-devel libdvdread-devel libdvdnav-devel libcdio-paranoia-devel libguess-devel lcms2-devel pulseaudio-libs-devel alsa-lib-devel libdrm-devel libX11-devel libvdpau-devel libcaca-devel mesa-libEGL-devel enca-devel libXScrnSaver-devel libXv-devel libXinerama-devel libXrandr-devel libva-devel libv4l perl-Math-BigInt perl-Math-BigRat youtube-dl luajit-devel openssl-devel
Requires: youtube-dl

# Don't build debug package
%define debug_package %{nil}

%description
Mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types. Special
input URL types are available to read input from a variety of sources other
than disk files. Depending on platform, a variety of different video and audio
output methods are supported.

%prep
%autosetup -n mpv-v0.26.0

%build
./rebuild -j$(($(nproc)+1))

%install
mkdir -p %{buildroot}/usr/bin
cp mpv/build/mpv %{buildroot}/usr/bin/

%files
/usr/bin/mpv

%changelog
* Wed Jun 22 2016 Martin Hagstrom <marhag87@gmail.com> 0.26.0
- Initial release

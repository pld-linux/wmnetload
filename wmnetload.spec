Summary:	A dockapp to monitor network interface usage
Summary(pl):	Aplikacja - dok do monitorowania u¿ycia interfejsu sieciowego
Name:		wmnetload
Version:	1.2
Release:	1
License:	GPL
Vendor:		Peter Mamishian <meem@gnu.org>
Group:		X11/Applications/Networking
Source0:	ftp://truffula.com/pub/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Icon:		backlight_on.xpm
BuildRequires:	libdockapp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Wmnetload is a network interface monitor dockapp for Window Maker. It
is designed to fit well with dockapps like wmcpuload and wmmemmon. It
tracks whether the interface is functioning and displays current
network interface throughput, along with an auto-scaling graph of
recent network activity.

%description -l pl
Wmnetload jest moniotrem interfejsu sieciowego, w postaci doku dla
Window Makera. Jest tak zaprojektowany, ¿eby pasowaæ do innych tego
typu aplikacji takich jak wmcpuload czy wmmwmmon. Zaznacza kiedy
interfejs funkcjonuje oraz wy¶wietla bie¿±c± przepustowo¶æ sieci, przy
pomocy automatycznie skaluj±cego siê wykresu ostatniej aktywno¶ci
sieci.

%prep
%setup -qn %{name}-%{version}

%build
OPTFLAGS="%{rpmcflags}" CC="%{__cc}"
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xbindir},%{_pixmapsdir},%{_applnkdir}/Network}

install src/wmnetload $RPM_BUILD_ROOT%{_xbindir}/wmnetload
install xpm/classic/backlight_down.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/backlight_down.xpm
install xpm/classic/backlight_err.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/backlight_err.xpm
install xpm/classic/backlight_off.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/backlight_off.xpm
install xpm/classic/backlight_on.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/backlight_on.xpm
install xpm/classic/parts.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/parts.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root)%{_bindir}/*
%{_applnkdir}/Network/wmnetload.desktop
%{_pixmapsdir}/*.xpm

Summary:	A dockapp to monitor network interface usage
Summary(pl.UTF-8):   Aplikacja-dok do monitorowania obciążenia interfejsu sieciowego
Name:		wmnetload
Version:	1.3
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://truffula.com/pub/%{name}-%{version}.tar.bz2
# Source0-md5:	f2a0507cd526ce2c6977ebe9252df81c
Source1:	%{name}.desktop
Patch0:		%{name}-config.patch
URL:		http://freshmeat.net/projects/wmnetload
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdockapp-devel >= 0.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmnetload is a network interface monitor dockapp for Window Maker. It
is designed to fit well with dockapps like wmcpuload and wmmemmon. It
tracks whether the interface is functioning and displays current
network interface throughput, along with an auto-scaling graph of
recent network activity.

%description -l pl.UTF-8
Wmnetload jest monitorem interfejsu sieciowego, w postaci doku dla
Window Makera. Jest tak zaprojektowany, żeby pasować do innych tego
typu aplikacji takich jak wmcpuload czy wmmemmon. Zaznacza kiedy
interfejs funkcjonuje oraz wyświetla bieżącą przepustowość sieci, przy
pomocy automatycznie skalującego się wykresu ostatniej aktywności
sieci.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}/docklets}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install xpm/classic/backlight_down.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/backlight_down.xpm
install xpm/classic/backlight_err.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/backlight_err.xpm
install xpm/classic/backlight_off.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/backlight_off.xpm
install xpm/classic/backlight_on.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/backlight_on.xpm
install xpm/classic/parts.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/parts.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/wmnetload.desktop
%{_pixmapsdir}/*.xpm

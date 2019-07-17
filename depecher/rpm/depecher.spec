# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       depecher

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Telegram client for Sailfish OS
Version:    0.6.1
Release:    2
Group:      Applications/Communications
License:    LICENSE
URL:        https://github.com/blacksailer/depecher
Source0:    %{name}-%{version}.tar.bz2
Source100:  depecher.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   tdlibjson >= 1.3.1
Requires:   libvorbis
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(tdlibjson)
BuildRequires:  pkgconfig(nemonotifications-qt5)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  desktop-file-utils

%description
Another Telegram client for Sailfish OS built on top of tdlib


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
%post
systemctl-user stop org.blacksailer.depecher.service || true
if /sbin/pidof depecher > /dev/null; then
killall depecher || true
fi

systemctl restart mce.service
systemctl-user restart ngfd.service
#Moving db dir issue - #14
if [ -d "/home/nemo/depecherDatabase" ]; then
if [ -e "/home/nemo/depecherDatabase/db.sqlite" ];then
mv /home/nemo/depecherDatabase /home/nemo/.local/share/harbour-depecher
fi
fi

systemctl-user daemon-reload
#systemctl-user enable org.blacksailer.depecher.service || true
#systemctl-user restart org.blacksailer.depecher.service || true

# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%preun
# >> preun
systemctl-user stop org.blacksailer.depecher.service || true
systemctl-user disable org.blacksailer.depecher.service || true
systemctl-user daemon-reload
if /sbin/pidof depecher > /dev/null; then
killall depecher || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/lipstick/notificationcategories/*.conf
%{_datadir}/ngfd/events.d/*.ini
%exclude %{_libdir}/cmake/*
%exclude %{_libdir}/debug/*
%{_datadir}/dbus-1/services/org.blacksailer.depecher.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/jolla-settings/entries/%{name}.json
%{_libdir}/systemd/user/org.blacksailer.depecher.service
%{_libdir}/nemo-transferengine/plugins/*
# >> files
# << files

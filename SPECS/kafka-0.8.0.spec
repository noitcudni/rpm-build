Name:          	kafka 
Version:       	0.8.0
Release:        1%{?dist}
Summary:        kafka 0.8.0 

License:        GPLv2+
Source0:       	%{name}_2.8.0-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}_2.8.0-%{version}
%description

%prep
%setup -n %{name}_2.8.0-%{version}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT/usr/lib/%{name}_2.8.0-%{version}
install -d $RPM_BUILD_ROOT/usr/lib/
cp -r ../%{name}_2.8.0-%{version} $RPM_BUILD_ROOT/usr/lib/.

%clean

%files
%defattr(-,root,root)
/usr/lib/%{name}_2.8.0-%{version}

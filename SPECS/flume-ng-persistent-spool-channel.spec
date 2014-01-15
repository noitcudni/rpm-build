Name:           flume-ng-persistent-spool-channel
Version:       	0.1.0
Release:        1%{?dist}
Summary:        Our custom flume persistent spool channel

License:        GPLv2+
URL: 		https://latesco.sea.kixeye.com/projects/AE/repos/v3/browse/flume-ng-persistent-spool-channel
Source0:        %{name}-%{version}.tgz

BuildRequires:  apache-maven
Requires: flume

%description


%prep
%setup -q


%build
mvn clean install -Dmaven.test.skip=true -Drat.numUnapprovedLicenses=100

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/flume/lib
install -m 644 target/%{name}-uber-0.0.1-SNAPSHOT.jar $RPM_BUILD_ROOT/usr/lib/flume/lib/%{name}-uber-0.0.1-SNAPSHOT.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/usr/lib/flume/lib/%{name}-uber-0.0.1-SNAPSHOT.jar


%changelog

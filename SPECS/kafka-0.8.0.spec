%define         gist_patch gist43c6d9f38795cca81c54-37a4546d20f6ba8ea07c7191abf903b7623efa13
%define         scala_version 2.8.0

Name:          	kafka 
Version:       	0.8
Release:        1%{?dist}
Summary:        kafka 0.8 

License:        GPLv2+
Source0:       	%{name}-%{version}.zip
Source1:	%{gist_patch}.tar.gz 

BuildRoot: %{_tmppath}/%{name}-%{version}
%description

%prep
%setup -n %{name}-%{version}

%build
tar xvzf $RPM_SOURCE_DIR/%{gist_patch}.tar.gz -C $RPM_BUILD_DIR
cp $RPM_BUILD_DIR/%{gist_patch}/* $RPM_BUILD_DIR/%{name}-%{version}/perf/src/main/scala/kafka/perf/.
./sbt clean && ./sbt update && ./sbt "++%{scala_version} package" && ./sbt assembly-package-dependency && ./sbt release-zip

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT/usr/lib/%{name}_2.8.0-%{version}
install -d $RPM_BUILD_ROOT/usr/lib/
cp -r $RPM_BUILD_DIR/%{name}-%{version}/target/RELEASE/%{name}_%{scala_version}-%{version}.0 $RPM_BUILD_ROOT/usr/lib/.

%clean

%files
%defattr(-,root,root)
/usr/lib/%{name}_%{scala_version}-%{version}.0

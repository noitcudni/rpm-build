%define         gist_patch gist43c6d9f38795cca81c54-37a4546d20f6ba8ea07c7191abf903b7623efa13
%define         scala_version 2.8.0

Name:          	kafka
Version:       	0.8.1
Release:        1%{?dist}
Summary:        kafka 0.8.1

License:        GPLv2+
Source0:       	%{name}-%{version}.zip

BuildRoot: %{_tmppath}/%{name}-%{version}
%description

%prep
%setup -n %{name}-%{version}

%build
#tar xvzf $RPM_SOURCE_DIR/%{gist_patch}.tar.gz -C $RPM_BUILD_DIR
#cp $RPM_BUILD_DIR/%{gist_patch}/* $RPM_BUILD_DIR/%{name}-%{version}/perf/src/main/scala/kafka/perf/.
./gradlew clean; ./gradlew releaseTarGz
#./sbt clean && ./sbt update && ./sbt "++%{scala_version} package" && ./sbt assembly-package-dependency && ./sbt release-zip

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/%{name}_%{scala_version}-%{version}
cp -r $RPM_BUILD_DIR/%{name}-%{version}/core/build/distributions/%{name}_%{scala_version}-%{version}.tgz $RPM_BUILD_ROOT/usr/lib/%{name}_%{scala_version}-%{version}
cd $RPM_BUILD_ROOT/usr/lib/%{name}_%{scala_version}-%{version}; tar xvzf $RPM_BUILD_ROOT/usr/lib/%{name}_%{scala_version}-%{version}/%{name}_%{scala_version}-%{version}.tgz
rm $RPM_BUILD_ROOT/usr/lib/%{name}_%{scala_version}-%{version}/*.tgz

%clean

%files
%defattr(-,root,root)
/usr/lib/%{name}_%{scala_version}-%{version}

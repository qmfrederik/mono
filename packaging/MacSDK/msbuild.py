import fileinput

class MSBuild (GitHubPackage):
	def __init__ (self):
		GitHubPackage.__init__ (self, 'mono', 'msbuild', '15',  # note: fix scripts/ci/run-test-mac-sdk.sh when bumping the version number
			revision = '8f608e49833cc1e2f6c9c070dacbd8fdcb41a20e')

	def build (self):
		self.sh ('./eng/cibuild_bootstrapped_msbuild.sh --host_type mono --configuration Release --skip_tests')
		self.sh ('find artifacts -wholename \'*/log/*\' -type f -exec zip msbuild-bin-logs.zip {} \+')

	def install (self):
		# use the bootstrap msbuild as the system might not have one available!
		self.sh ('./artifacts/mono-msbuild/msbuild mono/build/install.proj /p:MonoInstallPrefix=%s /p:Configuration=Release-MONO /p:IgnoreDiffFailure=true' % self.staged_prefix)

MSBuild ()

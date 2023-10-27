# Based on https://github.com/KyleKing/not-on-pypi
from pathlib import Path
from setuptools import setup
from setuptools.command.install import install

PACKAGE_NAME = "django-ansible-base"

VERSION = '0a1'

AUTHOR = 'Rick Elrod'
AUTHOR_EMAIL = 'rick@elrod.me'

package_init = Path(PACKAGE_NAME).resolve() / '__init__.py'
package_init.parent.mkdir(exist_ok=True)
package_init.write_text('"""Do nothing."""\n')

# --------------------------------------------------------------------------------------


class WrongPackageInstalledError(RuntimeError):
    """More specific error."""

    pass


class RaiseErrorPreInstall(install):
    """Customized setuptools install command - prints a friendly greeting."""

    def run(self):
        raise WrongPackageInstalledError(f"""
\n\n
'{PACKAGE_NAME}' is not currently released, but may be in the future.
\n\n
""")



if __name__ == '__main__':
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        packages=[PACKAGE_NAME],
        description = 'Reserved package',
        long_description = 'Reserved package',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        license = 'MIT',
        classifiers=['License :: OSI Approved :: MIT License'],
        cmdclass={
            'install': RaiseErrorPreInstall,
        },
    )

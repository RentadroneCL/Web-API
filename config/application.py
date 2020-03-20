from os import getenv
from pathlib import Path
from dotenv import load_dotenv

base_path = Path(".")  # Fully qualified path to the project root
env_path = base_path / ".env"  # Fully qualified path to the enviroment file
app_path = base_path.joinpath("app")  # The fully qualified path to the app folder
public_path = base_path.joinpath(
    "public"
)  # The fully qualified path to the public folder
storage_path = base_path.joinpath(
    "storage"
)  # The fully qualified path to the storage folder

load_dotenv(dotenv_path=env_path)

config = {
    # --------------------------------------------------------------------------
    # Application Name
    # --------------------------------------------------------------------------
    #
    # This value is the name of your application. This value is used when the
    # framework needs to place the application's name in a notification or
    # any other location as required by the application or its packages.
    "name": getenv("APP_NAME", None),
    # --------------------------------------------------------------------------
    # Application Environment
    # --------------------------------------------------------------------------
    #
    # This value determines the "environment" your application is currently
    # running in. This may determine how you prefer to configure various
    # services the application utilizes. Set this in your ".env" file.
    "env": getenv("APP_ENV", "production"),
    # --------------------------------------------------------------------------
    # Application URL
    # --------------------------------------------------------------------------
    #
    # This URL is used by the console to properly generate URLs when using
    # the Artisan command line tool. You should set this to the root of
    # your application so that it is used when running Artisan tasks.
    "url": getenv("APP_URL", "http://localhost"),
    # --------------------------------------------------------------------------
    # Application Debug Mode
    # --------------------------------------------------------------------------
    #
    # When your application is in debug mode, detailed error messages with
    # stack traces will be shown on every error that occurs within your
    # application. If disabled, a simple generic error page is shown.
    "debug": getenv("APP_DEBUG", False),
    # --------------------------------------------------------------------------
    # Encryption Key
    # --------------------------------------------------------------------------
    #
    # This key is used by the encrypter service and should be set
    # to a random, 32 character string, otherwise these encrypted strings
    # will not be safe. Please do this before deploying an application!
    "key": getenv("APP_KEY", None),
    # --------------------------------------------------------------------------
    # Cross-Origin Resource Sharing (CORS)
    # --------------------------------------------------------------------------
    #
    # The origin, or list of origins to allow requests from. The origin(s) may be
    # regular expressions, case-sensitive strings, or else an asterisk
    "origins": getenv("CORS_DOMAINS", "*"),
}

import atexit
import tempfile
from ctypes import WinError

from winrt.microsoft.ui.xaml import (
    Application,
    ApplicationInitializationCallbackParams,
    GridLength,
    GridUnitType,
    HorizontalAlignment,
    LaunchActivatedEventArgs,
    VerticalAlignment,
    Window,
)
from winrt.microsoft.ui.xaml.controls import (
    ColumnDefinition,
    CoreWebView2InitializedEventArgs,
    Grid,
    RowDefinition,
    WebView2,
)
from winrt.microsoft.web.webview2.core import CoreWebView2Environment
from winrt.microsoft.windows.applicationmodel.dynamicdependency.bootstrap import (
    InitializeOptions,
    initialize,
)
from winrt.runtime import ApartmentType, init_apartment
from winrt.system import box_int32
from winrt.windows.foundation import AsyncStatus, IAsyncAction, IAsyncOperation, Uri


def check_initialized(sender: WebView2, args: CoreWebView2InitializedEventArgs):
    # This can be useful debugging issues when the WebView2 control fails to
    # initialize (in which case, it will appear as empty black box).
    if args.exception.value:
        print("Initialization failed", WinError(args.exception.value))


class App(Application):
    def _on_launched(self, args: LaunchActivatedEventArgs) -> None:
        webview = WebView2()
        webview.source = Uri("https://pywinrt.readthedocs.io/en/latest/")
        webview.add_core_web_view2_initialized(check_initialized)

        # Grid is used to make the WebView2 control fill the window.
        # Equivalent to the following XAML:
        """
        <Grid>
            <Grid.RowDefinitions>
                <RowDefinition Height="Auto"/>
                <RowDefinition Height="*"/>
            </Grid.RowDefinitions>
            <Grid.ColumnDefinitions>
                <ColumnDefinition Width="*"/>
                <ColumnDefinition Width="Auto"/>
            </Grid.ColumnDefinitions>

            <WebView2 Grid.Row="1" Grid.ColumnSpan="2"
                HorizontalAlignment="Stretch" VerticalAlignment="Stretch"/>
        </Grid>
        """
        grid = Grid()
        auto_row = RowDefinition()
        auto_row.height = GridLength(1, GridUnitType.AUTO)
        grid.row_definitions.append(auto_row)
        star_row = RowDefinition()
        star_row.height = GridLength(1, GridUnitType.STAR)
        grid.row_definitions.append(star_row)
        star_col = ColumnDefinition()
        star_col.width = GridLength(1, GridUnitType.STAR)
        grid.column_definitions.append(star_col)
        auto_col = ColumnDefinition()
        auto_col.width = GridLength(1, GridUnitType.AUTO)
        grid.column_definitions.append(auto_col)
        webview.horizontal_alignment = HorizontalAlignment.STRETCH
        webview.vertical_alignment = VerticalAlignment.STRETCH
        webview.set_value(Grid.row_property, box_int32(1))
        webview.set_value(Grid.column_span_property, box_int32(2))
        grid.children.append(webview)

        window = Window()
        window.add_closed(lambda s, e: self.exit())
        window.content = grid

        # By default, WebView2 will create a directory in the .exe's directory
        # which isn't usually desireable. Here we create a temporary directory
        # since this is just example code. A real app would use some application-
        # specific user data directory and not delete it at exit.
        cache_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        atexit.register(cache_dir.cleanup)

        env_op = CoreWebView2Environment.create_with_options_async(
            "", cache_dir.name, None
        )

        def on_env(op: IAsyncOperation[CoreWebView2Environment], status: AsyncStatus):
            if status == AsyncStatus.ERROR:
                print(
                    "create_with_options_async failed:", WinError(op.error_code.value)
                )
                return

            if status != AsyncStatus.COMPLETED:
                return

            env = op.get_results()

            ensure_op = webview.ensure_core_web_view2_with_environment_async(env)

            def on_ensure(op: IAsyncAction, status: AsyncStatus):
                if status == AsyncStatus.ERROR:
                    print(
                        "ensure_core_web_view2_async failed:",
                        WinError(op.error_code.value),
                    )
                    return

                if status != AsyncStatus.COMPLETED:
                    return

                # Don't show the window until ready to avoid black box
                window.activate()

            ensure_op.completed = on_ensure

        env_op.completed = on_env


def init(_: ApplicationInitializationCallbackParams) -> None:
    # This implicitly sets Application.current to this object so we don't need
    # to keep a reference to it.
    App()


if __name__ == "__main__":
    init_apartment(ApartmentType.SINGLE_THREADED)

    # This is the main entry point for the application. To use the Windows App SDK
    # outside of a packaged app, you have to bootstrap it using the initialize
    # function. The ON_NO_MATCH_SHOW_UI option will show a dialog if the required
    # version of the Windows App runtime is not installed.
    with initialize(options=InitializeOptions.ON_NO_MATCH_SHOW_UI):
        Application.start(init)

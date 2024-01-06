from reactpy import component, html, run, hooks


@component
def Gallery(is_show, width, height):
    if is_show:
        return html.img(
            {
                "src": f"https://picsum.photos/{width}/{height}",
                "alt": "Ngetest ...",
            }
        )
    else:
        return html.h5("Gambar akan muncul kalau tombol di klik!!!")


@component
def Button(is_show, set_is_show):
    def show_image_handler(event):
        set_is_show(not is_show)

    return html.button({"onclick": show_image_handler}, f"muncul gambar: {is_show}")


@component
def App():
    is_show, set_is_show = hooks.use_state(False)

    return html._(
        html.h1("Nyoba pake reactpy"),
        Button(is_show, set_is_show),
        Gallery(is_show, width=190, height=180),
    )


run(App)

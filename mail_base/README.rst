Mail Base
=========

Modules doesn't introduce new features, but make built-in mail js features extendable.

Usage
-----
To use this module you need either install module that depends on it or create new module.

Further information
-------------------
Due to odoo restrictions, module makes mail initialization again. That is browser loads emoji and other chat data twice. This is the only way to make Mail feature extendable.

One can say, that the module do this todo from `addons/mail/static/src/js/chat_manager.js <https://github.com/odoo/odoo/blob/9.0/addons/mail/static/src/js/chat_manager.js#L57>`_

    // to do: move this to mail.utils

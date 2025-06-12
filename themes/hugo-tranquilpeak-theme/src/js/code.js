(function($) {
  'use strict';

    $(document).ready(function() {
        // Select each <pre><code> block
        $('pre code').each(function() {
            var $this = $(this);

            // Retrieve the value of the 'data-lang' attribute from the current <code> element
            var lang = $this.data('lang');

            // If a 'data-lang' attribute exists, create and prepend a language label
            if (lang) {
                var $langLabel = $('<div class="code-lang-label"></div>');
                $langLabel.text(lang);
                $this.parent().prepend($langLabel);
            }

            var originalSvg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="none"><path d="M3.33301 4V13.3333C3.33301 13.5101 3.40325 13.6797 3.52827 13.8047C3.65329 13.9298 3.82286 14 3.99967 14H10.6663M12.6663 4V11.3333H5.99967V2H10.6663L12.6663 4Z" stroke="#667176" stroke-linecap="round" stroke-linejoin="round"></path></svg>';
            var checkmarkSvg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="#000000" d="M18.71,7.21a1,1,0,0,0-1.42,0L9.84,14.67,6.71,11.53A1,1,0,1,0,5.29,13l3.84,3.84a1,1,0,0,0,1.42,0l8.16-8.16A1,1,0,0,0,18.71,7.21Z"></path></svg>';

            // Create a copy button
            var $button = $('<button class="copy-code-btn"></button>');
            $button.html(originalSvg);

            // Prepend the button to the <pre> tag (parent of code)
            $this.parent().append($button);

            // Add click event listener to the button
            $button.on('click', function() {
                var codeText = $this.text();
                navigator.clipboard.writeText(codeText);
                $button.html(checkmarkSvg);

                setTimeout(function() {
                    $button.html(originalSvg);
                }, 2000); // 2000 milliseconds = 2 seconds
            });
        });
    });
})(jQuery);
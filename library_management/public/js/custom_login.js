$(document).ready(function() {
    $('#login-form').on('submit', function(e) {
        e.preventDefault();
        
        const $form = $(this);
        const $btn = $('#login-btn');
        const $btnText = $btn.find('.btn-text');
        const $btnLoader = $btn.find('.btn-loader');
        
        const usr = $form.find('input[name="usr"]').val();
        const pwd = $form.find('input[name="pwd"]').val();
        
        $btn.prop('disabled', true);
        $btnText.hide();
        $btnLoader.show();
        
        $('.error-message').remove();
        
        $.ajax({
            url: '/api/method/login',
            type: 'POST',
            data: { usr: usr, pwd: pwd },
            success: function(response) {
                if (response.message === 'Logged In') {
                    window.location.href = '/app';
                }
            },
            error: function(xhr) {
                let errorMsg = 'Invalid username or password';
                
                if (xhr.responseJSON && xhr.responseJSON._server_messages) {
                    try {
                        const messages = JSON.parse(xhr.responseJSON._server_messages);
                        if (messages.length > 0) {
                            const msg = JSON.parse(messages[0]);
                            errorMsg = msg.message || errorMsg;
                        }
                    } catch (e) {
                        console.error('Error parsing message:', e);
                    }
                }
                
                $form.prepend('<div class="error-message show">' + errorMsg + '</div>');
                $btn.prop('disabled', false);
                $btnText.show();
                $btnLoader.hide();
            }
        });
    });
    
    $('#forgot-link').on('click', function(e) {
        e.preventDefault();
        const email = $('#username').val();
        
        if (!email) {
            alert('Please enter your email address first');
            $('#username').focus();
            return;
        }
        
        window.location.href = '/forgot-password?email=' + encodeURIComponent(email);
    });
});

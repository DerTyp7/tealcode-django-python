function accept_cookies(){
    document.cookie = "cookies_allowed=1;path=/";
    window.location.reload();
}

document.write('<div style="background-color: rgba(255, 255, 255, 0.219);" id="cookie_banner" class="text-center"><p>We only use non-technical cookies for analysis purposes.<br> Do you want to accept those cookies? (please)</p><button class="btn btn-success mb-3" onclick="accept_cookies()">Accept</button></div>');

cookies_allowed = document.cookie.split("cookies_allowed=")[1][0]

if(cookies_allowed == null){
    document.cookie = "cookies_allowed=0;path=/";
    cookies_allowed = document.cookie.split("cookies_allowed=")[1]
}
if(cookies_allowed == "1"){
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-PGM5LTFSMG');
    document.getElementById("cookie_banner").style.display = "none";
}else if(cookies_allowed == "0"){
    console.log("DO NOT LOAD ANALYTILCS");
}
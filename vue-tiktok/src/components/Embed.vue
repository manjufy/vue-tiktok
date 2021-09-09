<template>
    <div class="embed-responsive" v-if="valid" style="width: 900px; height: 900px">
        <iframe sandbox="allow-forms allow-scripts allow-pointer-lock allow-same-origin allow-top-navigation"
            class="embed-responsive-item" allowfullscreen :src="url">
        </iframe>
    </div>
</template>

<script>
    export default {
        props: {
            css: {
                type: String,
                default: 'embed-responsive-16by9'
            },
            src: { type: String },
            params: {
                type: Object
            },
        },
        data() {
            return {
                valid: false,
                url: '',
                videos: [
                    {
                        //reg: /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=|\?v=)([^#\&\?]*).*/i,
                        //reg: /^.*(?:(?:v|vi|be|videos|embed)\/(?!videoseries)|(?:v|ci)=)([\w-]{11})/i,
                        reg:/^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\\-]+\?v=|embed\/|v\/)?)([\w\\-]+)(\S+)?$/i,
                        url: 'https://www.youtube.com/embed/$5',
                        params: {
                            'picture-in-picture': 1,
                            accelerometer: 1,
                            gyroscope: 1
                        }
                    },
                ],
            }
        },
        watch: {
            src(val) {
                console.log('Val', val);
                this.parse();
            },
        },
        methods: {
            parse() {
                if (this.src) {
                    for (let i = 0; i < this.videos.length; i++) {
                        const v = this.videos[i];
                        var m = v.reg.exec(this.src);
                        if (m) {
                            var params = Object.assign({}, v.params, this.params);
                            var query = Object.keys(params).map(key => key + '=' + params[key]).join('&');
                            var and = v.url.indexOf('?') >= 0 ? '&' : '?';
                            this.url = this.src.replace(v.reg, v.url) + and + query;
                            this.valid = true;
                            return;
                        }
                    }
                }
                this.valid = false;
            },
        },
        mounted() {
            this.parse();
        }
    }
</script>
<style>
html, body {
    background-color: #fefefe;
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    margin: 0;
  }
  
  header {
    margin-top: 65px;
    text-align: center;
    padding: 6px;
  }
  
  header h1 {
    text-align: center;
    margin: 0 0 5px 0;
    font-weight: 900;
    font-size: 4rem;
    color: #34495e;
    font-family: 'Hammersmith One', sans-serif;
  }
  
  header h4 {
    color: #9E9E9E;
    text-align: center;
    margin: 0 0 35px 0;
    font-weight: 400;
    font-size: 24px;
    font-family: 'Athiti', sans-serif;
  }
  
  main {
    max-width: 525px;
    width: 100%;
    padding-top: 34px;
    margin: auto;
    height: 410px;
    font-size: 1rem;
    padding-bottom: 79px;
  }
  
  a {
    text-decoration: none;
    color: #34495e;
  }
  
  p {
    word-spacing: 0.05em;
  }
  
  footer {
    padding: 30px 0;
    color: #fff;
    text-align: center;
    font-weight: 300;
    font-family: 'Roboto', sans-serif;
    background: #34495e;
    font-size: 0.9rem;
    width: 100%;
    bottom: 0;
    left: 0;
  }
  
  footer .social-icon {
    margin: 0 7px;
  }
  
  footer .social-icon svg {
    width: 30px;
    height: 30px;
  }
  
  a:hover, footer .social-icon svg:hover {
    opacity: 0.6;
  }
  
  footer a {
    font-weight: 400;
    color: #fff;
  }
  footer img{
      height: 50px;
      margin-right: 8px;
  }
  

  
code[data-lang], pre[data-lang], pre[data-lang] code {
    text-shadow: 0 1px rgba(255, 255, 255, 0.3);
    direction: ltr;
    text-align: left;
    white-space: pre;
    word-spacing: normal;
    word-break: normal;
    word-wrap: normal;
    line-height: 1.5;
    -moz-tab-size: 3;
    -o-tab-size: 3;
    tab-size: 3;
    -webkit-hyphens: none;
    -moz-hyphens: none;
    -ms-hyphens: none;
    hyphens: none;
    border: none;
}

pre[data-lang] {
    padding: 1em;
    margin: .5em 0;
    overflow: auto;
    border-radius: .3em
}

:not(pre)>code[data-lang], pre[data-lang] {
    background: #eee
}

:not(pre)>code[data-lang] {
    padding: .1em;
    border-radius: .3em;
    white-space: normal
}

.embed-responsive-item {
    width: 85%;
    height: 350px;
}
</style>
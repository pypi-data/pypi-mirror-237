"use strict";(self.webpackChunkopensarlab_frontend=self.webpackChunkopensarlab_frontend||[]).push([[648],{648:(e,n,t)=>{t.r(n),t.d(n,{default:()=>g});var o=t(684),a=t(697),s=t(861),l=t(778);class i extends l.Widget{constructor(){super(),this.hyperlink=document.createElement("a"),this.hyperlink.text="OpenSARlab Docs",this.hyperlink.href="https://opensarlab-docs.asf.alaska.edu/user-guides/how_to_run_a_notebook/",this.hyperlink.target="blank",this.addClass("opensarlab-doc-link-widget"),this.addClass("opensarlab-frontend-object"),this.node.appendChild(this.hyperlink)}}var r=t(614),d=t(788);async function c(e="",n={}){const t=d.ServerConnection.makeSettings(),o=r.URLExt.join(t.baseUrl,"opensarlab-frontend",e);let a;try{a=await d.ServerConnection.makeRequest(o,n,t)}catch(e){throw new d.ServerConnection.NetworkError(e)}let s=await a.text();if(s.length>0)try{s=JSON.parse(s)}catch(e){console.log("Not a JSON response body.",a)}if(!a.ok)throw new d.ServerConnection.ResponseError(a,s.message||s);return s}class p extends l.Widget{constructor(){super(),this.span=document.createElement("span"),this.addClass("opensarlab-profile-label-widget"),this.addClass("opensarlab-frontend-object"),this.node.appendChild(this.span)}}var b=t(51),f=t.n(b);class u extends l.Widget{constructor(){super(),this.toastrLink=document.createElement("link"),this.toastrLink.rel="stylesheet",this.toastrLink.href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css",this.node.appendChild(this.toastrLink),document.head.insertAdjacentHTML("beforeend","<style>#toast-container>div{opacity:1;}</style>")}makeToast(e){f().options=e.options,e.data.forEach((e=>{f()[e.type](e.message,e.title)}))}notifications(e){c(`opensarlab-oslnotify?type=${e}`).then((e=>{this.makeToast(e)})).catch((e=>{console.log(`Error on GET /opensarlab-frontend/opensarlab-oslnotify.\n${e}`)}))}}const h={id:"opensarlab_frontend:plugin",description:"A JupyterLab extension.",autoStart:!0,optional:[o.ISettingRegistry],activate:(e,n)=>{n?Promise.all([e.restored,n.load(h.id)]).then((([,n])=>{async function t(n){await async function(e,n){var t;const o=null!==(t=n.get("gifcap_btn").composite)&&void 0!==t?t:n.default("gifcap_btn");let l=o.enabled,i=o.rank;const r="opensarlab-frontend-gitcap-btn",d=(0,a.find)(e.shell.widgets("top"),(e=>e.id===r));if(d&&d.dispose(),!l)return void console.log("JupyterLab extension opensarlab-frontend:gifcap_btn is not activated!");const c=new s.ToolbarButton({className:"opensarlab-gitcap-btn",label:"GIF Capture",onClick:()=>{window.open("https://gifcap.dev","_blank")},tooltip:"Create and download screen capture GIFs"});c.id=r,c.addClass("opensarlab-frontend-object"),e.shell.add(c,"top",{rank:i}),console.log("JupyterLab extension opensarlab-frontend:gifcap_btn is activated!")}(e,n),await async function(e,n){var t;const o=null!==(t=n.get("profile_label").composite)&&void 0!==t?t:n.default("profile_label");let s=o.enabled,l=o.rank;const i="opensarlab-profile-label-widget",r=(0,a.find)(e.shell.widgets("top"),(e=>e.id===i));if(r&&r.dispose(),!s)return void console.log("JupyterLab extension opensarlab-frontend:profile_label is not activated!");let d=null;try{d=await c("opensarlab-profile-label"),console.log(d);const n=new p;n.id=i,n.span.innerText=d.data,e.shell.add(n,"top",{rank:l}),console.log("JupyterLab extension opensarlab-frontend:profile_label is activated!")}catch(e){console.error(`Error on GET /opensarlab-frontend/opensarlab-profile-label.\n${e}`)}}(e,n),await async function(e,n){var t;const o=null!==(t=n.get("doc_link").composite)&&void 0!==t?t:n.default("doc_link");let s=o.enabled,l=o.rank;const r="opensarlab-doc-link-widget",d=(0,a.find)(e.shell.widgets("top"),(e=>e.id===r));if(d&&d.dispose(),!s)return void console.log("JupyterLab extension opensarlab-frontend:doc_link is not activated!");const c=new i;c.id=r,e.shell.add(c,"top",{rank:l}),console.log("JupyterLab extension opensarlab-frontend:doc_link is activated!")}(e,n),await async function(e,n){var t;const o=null!==(t=n.get("controlbtn").composite)&&void 0!==t?t:n.default("controlbtn");let l=o.enabled,i=o.rank;const r="opensarlab-controlbtn",d=(0,a.find)(e.shell.widgets("top"),(e=>e.id===r));if(d&&d.dispose(),!l)return void console.log("JupyterLab extension opensarlab-frontend:controlbtn is not activated!");const c=new s.ToolbarButton({className:"opensarlab-controlbtn",label:"Shutdown and Logout Page",onClick:()=>{window.location.href="/hub/home"},tooltip:"Hub Control Panel: A place to stop the server and logout"});c.id=r,c.addClass("opensarlab-frontend-object"),e.shell.add(c,"top",{rank:i}),console.log("JupyterLab extension opensarlab-frontend:controlbtn is activated!")}(e,n),await async function(e,n){var t;const o=null!==(t=n.get("oslnotify").composite)&&void 0!==t?t:n.default("oslnotify");let s=o.enabled,l=o.note_type;const i="opensarlab-notify-widget",r=(0,a.find)(e.shell.widgets("top"),(e=>e.id===i));if(r&&r.dispose(),!s)return void console.log("JupyterLab extension opensarlab-frontend:oslnotify is not activated!");const d=new u;d.id=i,d.notifications(l),e.shell.add(d,"top",{rank:1999}),console.log("JupyterLab extension opensarlab-frontend:oslnotify is activated!")}(e,n)}t(n),n.changed.connect(t),console.log("JupyterLab extension opensarlab_frontend is fully operational!")})).catch((e=>{console.error(`Something went wrong...${e}`)})):console.log("Settings not found. opensarlab_frontend cannot be established.")}},g=h}}]);
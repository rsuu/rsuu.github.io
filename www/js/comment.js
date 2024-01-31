let vec_comment = document.querySelectorAll("#vec-comment > .comment");

let class_comment_marl = "--comment-marl";
let class_header_hide = "--comment-header-hide";
let class_body_hide = "--comment-body-hide";
let class_footer_hide = "--comment-footer-hide";
let class_btn_hide = "--comment-btn-hide";

let mut_flag_hide = false;

vec_comment.forEach(function (e) {
  let btn = e.querySelector(".btn");

  btn.addEventListener("click", function () {
    show_reply_only(e);
  });
});

function show_reply_only(self) {
  let tmp = self.getAttribute("js-vec-reply-from");

  if (mut_flag_hide || tmp == "") {
    // reset all
    vec_comment.forEach(function (element) {
      let comment = element.classList;
      let header = element.querySelector(".header").classList;
      let body = element.querySelector(".body").classList;
      //let footer = element.querySelector(".footer").classList;
      //let btn = element.querySelector(".btn").classList;

      comment.remove(class_comment_marl);
      header.remove(class_header_hide);
      body.remove(class_body_hide);
      //footer.remove(class_footer_hide);
    });
  }

  mut_flag_hide = !mut_flag_hide;

  if (tmp == "") {
    return;
  }

  let vec = tmp.split(",");

  //console.log(vec);

  let mut_idx = 0;
  vec_comment.forEach((element, id) => {
    let reply_id = vec[mut_idx];

    let comment = element.classList;
    let header = element.querySelector(".header").classList;
    let body = element.querySelector(".body").classList;
    //let footer = element.querySelector(".footer").classList;
    //let btn = element.querySelector(".btn").classList;

    if (id == reply_id) {
      comment.toggle(class_comment_marl);

      mut_idx += 1;
    } else {
      header.toggle(class_header_hide);
      body.toggle(class_body_hide);
      //footer.toggle(class_footer_hide);
    }

    //btn.toggle(class_btn_hide);
  });

  let self_header = self.querySelector(".header").classList;
  let self_body = self.querySelector(".body").classList;
  //let self_footer = self.querySelector(".footer").classList;
  //let self_btn = self.querySelector(".btn");

  self.classList.remove(class_comment_marl);
  self_header.remove(class_header_hide);
  self_body.remove(class_body_hide);
  //self_footer.remove(class_footer_hide);
}

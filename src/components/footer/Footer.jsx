import "./footer.css";
import NavBar from "../navbar/NavBar";

export default function Footer() {
  return (
      <div className="footer">
          <div className="footerLeft">
              <div className="footerList">All Rights Reserved © 2024 STYLAZAR</div>
          </div>
          <div className="footerRight">
              <div className="footerRightList">
                  <h3 className="footerRightTitle">Follow Us</h3>
                  <i className="footerIcon fa-brands fa-linkedin"></i>
                  <i className="footerIcon fa-brands fa-facebook"></i>
                  <i className="footerIcon fa-brands fa-square-x-twitter"></i>
                  <i className="footerIcon fa-brands fa-instagram"></i>
                  <i className="footerIcon fa-brands fa-square-github"></i>
              </div>
          </div>
    </div>
  )
}
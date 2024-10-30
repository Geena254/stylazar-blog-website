import "./navbar.css"
import { Link } from "react-router-dom";

export default function NavBar() {
    const user = true;
  return (
    <div className="nav">
        <div className="navleft">
            <Link className="Link" to="/landingpage">STYLAZAR</Link>
            <div className="navSearch">
                <i className="navSearchIcon fa-solid fa-magnifying-glass"></i>
            </div>
        </div>
        <div className="navcenter">
            <ul className="navList">
                <li className="navListItem">
                    <Link className="Link" to="/">FEED</Link>
                </li>
                <li className="navListItem">
                    <Link className="Link" to="/createpost">CREATE POST</Link>
                </li>
                <li className="navListItem">
                    <Link className="Link" to="/setting">PROFILE</Link>
                </li>
            </ul>
        </div>
        <div className="navright">
            {
                user ? (
                    <div className="navLinks">
                        <img
                            className="navImg"
                            src="../../assets/"
                            alt=""
                        />
                            <li className="navListItem">
                                {user && "SIGNOUT"}
                            </li>
                    </div>
                ) : (
                    <ul className="navList">
                        <li className="navListItem">
                            <Link className="Link" to="/signin">SIGNIN</Link>
                        </li>
                        <li className="navListItem">
                            <Link className="Link" to="/register">GET STARTED</Link>
                        </li>
                    </ul>
                )
            }
        </div>
    </div>
  )
}

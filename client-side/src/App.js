import NavBar from "./components/navbar/NavBar";
import Register from "./pages/register/Register";
import Home from "./pages/home/Home";
import SinglePost from "./components/SinglePost/SinglePost";
import Signin from "./pages/signin/Signin";
import Footer from "./components/footer/Footer";
import CreatePost from "./pages/createpost/CreatePost";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Outlet } from 'react-router-dom';
import Post from "./components/post/Post";
import Landingpage from "./components/landingpage/landingpage";
import ErrorPage from "./pages/errorpage/ErrorPage";
import Profile from "./pages/profile/Profile";

export default function App() {
  const user = true;
  return (
    <Router>
      <NavBar />
      <Outlet />
      <Routes>
        <Route path="/landingpage" element={<Landingpage />} />
        <Route path="/" element={user? <Home /> : <Register />} />
        <Route path="/register" element={user ? <Home /> : <Register />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/signin" element={<Signin />} />
        <Route path="/createpost" element={<CreatePost />} />
        <Route path="/post" element={<Post />} />
        <Route path="/SinglePost/:postId" element={<SinglePost />} />
      </Routes>
      <Footer />
    </Router>
  );
}


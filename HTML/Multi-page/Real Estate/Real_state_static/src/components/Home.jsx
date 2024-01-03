import { ReactComponent as Logo} from '../assets/Icons/Logo.svg'

const Home = () => {

  return (
    <>
    <header>
      <nav>
        <img src={Logo} alt="logo img" />
        {/* nav link */}
        <ul>
          <li><a href="#">Location</a></li>
          <li><a href="#">Blogs</a></li>
          <li><a href="#">Testimonial</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>


    </header>
    </>
  )
}

export default Home
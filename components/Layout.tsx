import Head from 'next/head'
import Link from 'next/link'

import Menu from './Menu';

type MainProps = { title: string, isHome: boolean, children?: any };
type HeaderProps = { isHome: boolean };

const injectGA = () => {
    if (typeof window == 'undefined') {
        return;
      }
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        window.dataLayer.push(arguments);
      }
      gtag('js', new Date());
    
      gtag('config','G-CGRVC93M1H');
}

export default function Layout(props: MainProps) {
    return (
        <div>
            <Head>
                <title> {props.title} </title>
                <script>{injectGA()}</script>
            </Head>

            <Header isHome={props.isHome} />

            <Menu />

            <main>
                {props.children}
            </main>

            <footer className="shadow-outter h-auto py-2 flex justify-center bg-blue-300">
                <div>
                    <div className="justify-center py-4 space-x-4">
                        <Link href="https://paypal.me/kreimben">
                            <a className="bg-red-400 font-mono px-1 py-1" target="_blank">Paypal</a>
                        </Link>

                        <Link href="https://instagram.com/kreimben/">
                            <a className="bg-red-400 font-mono px-1 py-1" target="_blank">Instagram</a>
                        </Link>

                        <Link href="https://github.com/kreimben">
                            <a className="bg-red-400 font-mono px-1 py-1" target="_blank">Github</a>
                        </Link>
                    </div>
                    <p className="font-mono text-sm mb-8 pt-4">Copyright(C) 2019 - 2021. Aksidion Kreimben. All right reserved.</p>
                </div>
            </footer>

        </div>
    )
}

function Header(props: HeaderProps) {
    if (props.isHome) {
        return (
            <HomeHeader />
        );
    } else {
        return (
            <JustHeader />
        );
    }
}

function HomeHeader() {
    return (
        <div>
            <header className="text-center bg-fixed bg-center h-screen items-center">
                <div className="flex justify-center pt-8 pb-8">
                    <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40 shadow-2xl"></img>
                </div>
                <p className="text-2xl font-light font-mono bg-white bg-opacity-50 rounded-lg px-3 py-2 inline-block">Kreimben.com, Indie developer's website</p>
            </header>
            <style jsx>
                {`
                
                header {
                    background-image: url('/images/backgroundImage.jpg');
                }
                
                `}
            </style>
        </div>
    );
}

function JustHeader() {
    return (
        <div>
            <header className="text-center bg-cover bg-center h-auto items-center">
                <div className="flex justify-center py-8">
                    <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40 shadow-2xl"></img>
                </div>
                <p className="text-2xl font-light font-mono bg-white bg-opacity-50 rounded-lg px-3 py-2 mb-8 inline-block">Kreimben.com, Indie developer's website</p>
            </header>
            <style jsx>
                {`
                
                header {
                    background-image: url('/images/backgroundImage.jpg');
                }
                
                `}
            </style>
        </div>
    );
}
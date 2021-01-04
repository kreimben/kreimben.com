import Layout from '../components/Layout'
import { backgroundColor, textColor } from '../styles/globalColorSets';

export default () => (
    <>
        <Layout title="Kreimben::Home" isHome={true}>
            <div className="flex justify-center text-center">
                <div className="bg-gray-300 p-8 m-12 rounded-lg w-4/5 text-4xl font-serif">
                                Welcome to indie developer's website!
                </div>
            </div>
            <main className="flex justify-center">
                <div className="w-4/5 py-32 mb-12 shadow-xl rounded-lg text-center" style={{backgroundColor:backgroundColor}}>
                    <p className="text-4xl font-serif" style={{color:textColor}} >I code</p>
                    <p className="font-semibold text-5xl" style={{color:textColor}} >iOS, Front-End and anything!</p>
                </div>
            </main>
        </Layout>
    </>
)
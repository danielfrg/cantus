//
//  SongDetail.swift
//  Cantus
//
//  Created by Daniel Rodriguez on 4/5/21.
//

import SwiftUI
import SwiftySound

struct SongDetail: View {
    var song: Song
    
    var body: some View {
        if let urlPath = Bundle.main.url(forResource: song.source, withExtension: "mp3") {
            let mySound = Sound(url: urlPath!)
            mySound?.play()
        }
        
        Text(song.name)
    }
}

struct SongDetail_Previews: PreviewProvider {
    static var previews: some View {
        SongDetail(song: songs[0])
    }
}

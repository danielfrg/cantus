//
//  Song.swift
//  Cantus
//
//  Created by Daniel Rodriguez on 4/5/21.
//

import Foundation

struct Song: Hashable, Codable, Identifiable {
    var id: Int
    var name: String
    var source: String
    var bass: String
    var drums: String
    var other: String
    var vocals: String
}

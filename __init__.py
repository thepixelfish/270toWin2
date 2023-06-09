# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Braces_Election
                                 A QGIS plugin
 This is a plugin that will simulat Mr. Squiggly Braces Election
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-04-16
        copyright            : (C) 2023 by Claire Perez, Vasu Seth, Luke Turner, Diego Castro
        email                : perez.555@osu.edu
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Braces_Election class from file Braces_Election.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .braces_election import Braces_Election
    return Braces_Election(iface)

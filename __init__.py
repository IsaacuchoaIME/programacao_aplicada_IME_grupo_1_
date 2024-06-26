# -*- coding: utf-8 -*-
"""

/***************************************************************************
 ProgramacaoAplicadaGrupo3
                                 A QGIS plugin
 Solução do Grupo 3
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2024-06-16
        copyright            : (C) 2023 by Grupo 1
        email                : gustavo.ferreira07@ime.eb.br
                                mathetheussilva@ime.eb.br
                                uchoalzac@ime.eb.br
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

__author__ = 'Grupo 1'
__date__ = '2024-06-16'
__copyright__ = '(C) 2024 by Grupo 1'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ProgramacaoAplicadaGrupo1 class from file ProgramacaoAplicadaGrupo1.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .programacao_aplicada_grupo_1 import ProgramacaoAplicadaGrupo1Plugin
    return ProgramacaoAplicadaGrupo1Plugin()

#ifndef __XRDNETPMARK__
#define __XRDNETPMARK__
/******************************************************************************/
/*                                                                            */
/*                        X r d N e t P M a r k . h h                         */
/*                                                                            */
/* (c) 2021 by the Board of Trustees of the Leland Stanford, Jr., University  */
/*                            All Rights Reserved                             */
/*   Produced by Andrew Hanushevsky for Stanford University under contract    */
/*              DE-AC02-76-SFO0515 with the Department of Energy              */
/*                                                                            */
/* This file is part of the XRootD software suite.                            */
/*                                                                            */
/* XRootD is free software: you can redistribute it and/or modify it under    */
/* the terms of the GNU Lesser General Public License as published by the     */
/* Free Software Foundation, either version 3 of the License, or (at your     */
/* option) any later version.                                                 */
/*                                                                            */
/* XRootD is distributed in the hope that it will be useful, but WITHOUT      */
/* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or      */
/* FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public       */
/* License for more details.                                                  */
/*                                                                            */
/* You should have received a copy of the GNU Lesser General Public License   */
/* along with XRootD in a file called COPYING.LESSER (LGPL license) and file  */
/* COPYING (GPL license).  If not, see <http://www.gnu.org/licenses/>.        */
/*                                                                            */
/* The copyright holder's institutional names and contributor's names may not */
/* be used to endorse or promote products derived from this software without  */
/* specific prior written permission of the institution or contributor.       */
/******************************************************************************/

class XrdNetAddrInfo;
class XrdSecEntity;

class XrdNetPMark
{
public:

class Handle
     {public:

      bool        getEA(int &ec, int &ac)
                       {if (eCode >= 0) {ec = eCode; ac = aCode; return true;}
                        ec = ac = 0; return false;
                       }

      bool        Valid() {return eCode >= 0;}

                  Handle(const char *app=0, int ecode=0, int acode=0)
                        : appName(app), eCode(ecode), aCode(acode) {}

                  Handle(Handle &h)
                        : appName(h.appName), eCode(h.eCode), aCode(h.aCode) {};

      virtual    ~Handle() {};

      protected:
      const char *appName;
      int         eCode;
      int         aCode;
     };

virtual Handle *Begin(XrdSecEntity &Client, const char *path=0,
                                            const char *cgi=0,
                                            const char *app=0) = 0;

virtual Handle *Begin(XrdNetAddrInfo &addr, Handle     &handle,
                                            const char *tident) = 0;

static  bool    getEA(const char *cgi, int &ecode, int &acode);

                XrdNetPMark() {}

static const int maxTotID = 0x7fff;

protected:

// ID limits and specifications
//
static const int btsActID =   6;
static const int mskActID =  63;
static const int maxActID =  63;

static const int maxExpID = 511;

virtual        ~XrdNetPMark() {} // This object cannot be deleted!
};
#endif
